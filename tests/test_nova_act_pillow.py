"""Optional compatibility checks for the Nova Act consumer of this fork."""

from importlib import import_module
from importlib.metadata import requires, version

import pytest
from packaging.requirements import Requirement
from PIL import Image

pytest.importorskip("nova_act")


def test_nova_act_dependency_constraints():
    assert version("strands-agents-tools") == "0.2.22+onsetto.1"
    assert version("pillow") == "13.0.0"
    for distribution in ("nova-act", "strands-agents-tools"):
        for dependency in requires(distribution):
            requirement = Requirement(dependency)
            if requirement.marker and not requirement.marker.evaluate():
                continue
            assert requirement.specifier.contains(version(requirement.name)), dependency


@pytest.mark.parametrize("namespace", ["nova_act", "nova_act.asyncio"])
@pytest.mark.parametrize("image_format", ["jpeg", "png"])
def test_nova_act_screenshot_round_trip_and_resize(namespace, image_format):
    helpers = import_module(f"{namespace}.tools.browser.default.util.image_helpers")
    image = Image.new("RGB", (16, 8), (20, 40, 60))
    data_url = helpers.convert_image_to_data_url(image, image_format)

    decoded = helpers.get_source_image_from_data_url(data_url)
    decoded.load()
    assert decoded.size == (16, 8)
    assert decoded.format.lower() == image_format

    resized_url = helpers.resize_image(data_url, {"width": 8, "height": 4})
    resized = helpers.get_source_image_from_data_url(resized_url)
    resized.load()
    assert resized.size == (8, 4)
    assert helpers.compare_images(data_url, resized_url) == 0
