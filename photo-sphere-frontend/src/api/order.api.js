import httpClient from './httpClient';

const END_POINT = '/order';

const placeOrder = (data) => httpClient.post(`${END_POINT}/`, data);

const getOrder = (id) => httpClient.get(`${END_POINT}/${id}/`);

export {
    placeOrder,
    getOrder
}