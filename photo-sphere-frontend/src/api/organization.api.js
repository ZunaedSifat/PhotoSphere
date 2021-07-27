import httpClient from './httpClient';

const END_POINT = '/organization';


const createOrganization = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

const getAllOrganizations = () => httpClient.get(`${END_POINT}/`);

const getOrganizationDetails = (id) => httpClient.get(`${END_POINT}/${id}/`);

const getOrganizationMembers = (id) => httpClient.get(`${END_POINT}/member/`, {
    params: {
        organization: id,
    }
});

const createOrganizationMember = (data) => httpClient.post(`${END_POINT}/member/`, data);

export {
    createOrganization,
    getAllOrganizations,
    getOrganizationDetails,
    getOrganizationMembers,
    createOrganizationMember
}