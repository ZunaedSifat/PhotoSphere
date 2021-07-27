import httpClient from './httpClient';

const END_POINT = '/order';

const placeOrder = (data) => httpClient.post(`${END_POINT}/`, data);

export {
    placeOrder
}