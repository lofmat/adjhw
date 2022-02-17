#!/usr/bin/env python3
import logging
import pytest
from task3.utils.req import Request
from task3.utils.data import Data


@pytest.fixture()
def suite_setup():
    req = Request()
    td = Data()
    return req, td


def test_create_pet(suite_setup):
    req, td = suite_setup[0], suite_setup[1]
    data = td.init_data(keys_to_replace={'id': 100}, data_type='pet')
    logging.info(f'Data input: {data}')
    resp_post = req.post_request(endpoint='pet', post_data=data)
    assert resp_post['code'] == 200 and resp_post['content'] == data
    resp_get = req.get_request(endpoint=f'pet/{100}')
    assert resp_get['code'] == 200 and resp_get['content'] == data


def test_update_pet_resp_400(suite_setup):
    req, td = suite_setup[0], suite_setup[1]
    data = td.init_data(keys_to_replace={'id': 101, 'name': 'Max'}, data_type='pet')
    logging.info(f'Data input: {data}')
    resp_post = req.post_request(endpoint='pet', post_data=data)
    assert resp_post['code'] == 200 and resp_post['content'] == data
    data['id'] = 10000
    resp_put = req.put_request(endpoint='pet', put_data=data)
    assert resp_put['code'] == 400


def test_create_store(suite_setup):
    req, td = suite_setup[0], suite_setup[1]
    data = td.init_data(keys_to_replace={'id': 100, 'petId': 201, "quantity": 10}, data_type='store')
    logging.info(f'Data input: {data}')
    resp_post = req.post_request(endpoint='store/order', post_data=data)
    assert resp_post['code'] == 200 and resp_post['content'] == data
    resp_get = req.get_request(endpoint=f'store/order/{100}')
    assert resp_get['code'] == 200 and resp_get['content'] == data


def test_order_delete(suite_setup):
    req, td = suite_setup[0], suite_setup[1]
    data = td.init_data(keys_to_replace={'id': 102, 'petId': 201, "quantity": 10}, data_type='store')
    logging.info(f'Data input: {data}')
    resp_post = req.post_request(endpoint='store/order', post_data=data)
    assert resp_post['code'] == 200
    req.delete_request(endpoint='store/order/102')
    resp_get = req.get_request(endpoint=f'store/order/{102}')
    assert resp_get['code'] == 404

