import httpClient from './httpClient';

const END_POINT = '/photo';

// used to update current user's profile information
const uploadPhoto = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

const getOwnPhotos = (user) => httpClient.get(`${END_POINT}/`, {
    params: {
        'user': user
    }
});

const getPhotoDetails = (id) => httpClient.get(`${END_POINT}/${id}`);

export {
    uploadPhoto,
    getOwnPhotos,
    getPhotoDetails,
}