import httpClient from './httpClient';

const END_POINT = '/exhibition';

const createExhibition = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

const getAllExhibitions = () => httpClient.get(`${END_POINT}/`);

const getOrganizationExhibitions = (organization) => httpClient.get(`${END_POINT}/`, {
    params: {
        organizer: organization
    }
});

const createExhibitionEntry = (data) => httpClient.post(`${END_POINT}/entry/`, data);

const getExhibitionEntries = (exhibition) => httpClient.get(`${END_POINT}/entry/`, {
    params: {
        exhibition
    }
});

const getExhibitionDetails = (id) => httpClient.get(`${END_POINT}/${id}/`);

export {
    createExhibition,
    getAllExhibitions,
    getOrganizationExhibitions,
    createExhibitionEntry,
    getExhibitionEntries,
    getExhibitionDetails
}