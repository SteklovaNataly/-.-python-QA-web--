import yaml
import requests

with open("config.yaml", "r") as f:
    data = yaml.safe_load(f)


def test_1(login, find_id):
    res = requests.get(data["address"], params={"owner":"notMe"}, headers={"X-Auth-Token": login})
    list_id = [i["id"] for i in res.json()["data"]]
    assert find_id in list_id, "test_1 failed"


def test_2(login, title, description, content, find_description):
    res1 = requests.post(data["address"], params={"title": title, "description": description, "content": content},
                         headers={"X-Auth-Token": login})
    res2 = requests.get(data["address"], params={"description": find_description}, headers={"X-Auth-Token": login})
    assert res1 and res2, "test_2 failed"