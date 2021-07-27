import httpClient from './httpClient';

const END_POINT = '/exhibition';

const createExhibition = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

const getOrganizationExhibitions = (organization) => httpClient.get(`${END_POINT}/`);

export {
    createExhibition,
}