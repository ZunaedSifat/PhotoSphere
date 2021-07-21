import httpClient from './httpClient';

const END_POINT = '/photo/tag';


const createTag = (data) => httpClient.post(`${END_POINT}/`, data);

const getTag = (id) => httpClient.get(`${END_POINT}/${id}/`);

const getAllTags = () => httpClient.get(`${END_POINT}/`);


export {
    createTag,
    getTag,
    getAllTags
}