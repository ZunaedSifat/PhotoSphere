import httpClient from './httpClient';

const END_POINT = '/album';


const createAlbum = (data) => httpClient.post(`${END_POINT}/`, data);

const getUserAlbums = (user) => httpClient.get(`${END_POINT}/`, {
    params: {
        'user_id': user
    }
});

const getAlbumDetails = (id) => httpClient.get(`${END_POINT}/${id}`);

export {
    createAlbum,
    getUserAlbums,
    getAlbumDetails,
}