import pytest
import os
import json
import yaml
import GabesPythonToolBox.Utility.ConfigManager as CM

# Helper Functions

def write_config(file_path, data):
    """Write a JSON or YAML file for testing."""
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, "w", encoding="utf-8") as f:
        if ext == ".json":
            json.dump(data, f, indent=4)
        elif ext in [".yaml", ".yml"]:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)
        else:
            raise ValueError("Unsupported test config type")

def read_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)



# University-Inspired Sample Config


SAMPLE_CONFIG = {
    "university": {
        "name": "GTB University",
        "department": "Robotics Engineering"
    },
    "students": [
        {"id": 1, "name": "Alice", "project": "Autonomous Rover"},
        {"id": 2, "name": "Bob", "project": "Drone Swarm Control"}
    ],
    "projects": {
        "active": [
            {"title": "Autonomous Rover", "progress": 65, "supervisor": "Dr. Grey"},
            {"title": "Drone Swarm Control", "progress": 40, "supervisor": "Dr. Lin"}
        ],
        "completed": []
    },
    "lab_settings": {
        "open_hours": "08:00-18:00",
        "max_students": 10,
        "equipment": {
            "3D_printers": 2,
            "robots": ["Atlas", "Spot", "Rover"]
        }
    }
}



#Core Functionality Tests

@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_load_and_call(tmp_path, ext):
    file = tmp_path / f"lab_config{ext}"
    write_config(file, SAMPLE_CONFIG)

    cm = CM.ConfigManager(str(file))
    config = cm()
    assert config["university"]["name"] == "GTB University"
    assert config["students"][0]["name"] == "Alice"
    assert isinstance(config, dict)


@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_update_nested_and_indexed_keys(tmp_path, ext):
    file = tmp_path / f"update_test{ext}"
    write_config(file, SAMPLE_CONFIG)
    cm = CM.ConfigManager(str(file))

    # Update simple nested key
    cm.update("university.department", "Artificial Intelligence")
    assert cm.config["university"]["department"] == "Artificial Intelligence"

    # Update list item by index
    cm.update("students[1].project", "AI Ethics Research")
    assert cm.config["students"][1]["project"] == "AI Ethics Research"

    # Update deeply nested dictionary key
    cm.update("lab_settings.equipment.3D_printers", 3)
    assert cm.config["lab_settings"]["equipment"]["3D_printers"] == 3


@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_save_and_reload_same_format(tmp_path, ext):
    file = tmp_path / f"save_test{ext}"
    write_config(file, SAMPLE_CONFIG)
    cm = CM.ConfigManager(str(file))

    cm.update("projects.active[0].progress", 90)
    new_file = tmp_path / f"saved{ext}"
    cm.save(str(new_file))
    assert new_file.exists()

    reloaded = CM.ConfigManager(str(new_file))()
    assert reloaded["projects"]["active"][0]["progress"] == 90


@pytest.mark.parametrize("ext_from, ext_to", [
    (".json", ".yaml"),
    (".yaml", ".json"),
    (".yml", ".json"),
])
def test_cross_format_save(tmp_path, ext_from, ext_to):
    file = tmp_path / f"cross{ext_from}"
    write_config(file, SAMPLE_CONFIG)
    cm = CM.ConfigManager(str(file))

    cm.update("university.name", "Techville Institute of Robotics")
    out_file = tmp_path / f"converted{ext_to}"
    cm.save(str(out_file))

    assert out_file.exists()
    loaded = read_json(out_file) if ext_to == ".json" else read_yaml(out_file)
    assert loaded["university"]["name"] == "Techville Institute of Robotics"


@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_reset_to_original(tmp_path, ext):
    file = tmp_path / f"reset_test{ext}"
    write_config(file, SAMPLE_CONFIG)
    cm = CM.ConfigManager(str(file))

    cm.update("students[0].name", "Charlie")
    assert cm.config["students"][0]["name"] == "Charlie"

    cm.reset()
    assert cm.config["students"][0]["name"] == "Alice"


@pytest.mark.parametrize("ext", [".json", ".yaml", ".yml"])
def test_start_config_manager_factory(tmp_path, ext):
    file = tmp_path / f"factory_test{ext}"
    write_config(file, SAMPLE_CONFIG)

    cm = CM.startConfigManager(str(file))
    assert isinstance(cm, CM.ConfigManager)
    assert cm()["projects"]["active"][1]["title"] == "Drone Swarm Control"



#Error Handling Tests


def test_missing_file_raises(tmp_path):
    missing = tmp_path / "not_found.json"
    with pytest.raises(FileNotFoundError):
        CM.ConfigManager(str(missing))


def test_invalid_extension_raises(tmp_path):
    bad_file = tmp_path / "config.txt"
    bad_file.write_text("not a valid format", encoding="utf-8")
    with pytest.raises(ValueError):
        CM.ConfigManager(str(bad_file))


def test_invalid_json_content_raises(tmp_path):
    bad_file = tmp_path / "broken.json"
    bad_file.write_text("{ bad json data", encoding="utf-8")
    with pytest.raises(Exception):
        CM.ConfigManager(str(bad_file))