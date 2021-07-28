import httpClient from './httpClient';

const END_POINT = '/photo';

// used to update current user's profile information
const uploadPhoto = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

const getUserPhotos = (user) => httpClient.get(`${END_POINT}/`, {
    params: {
        'user': user
    }
});

const getFilteredPhotos = (params) => httpClient.get(`${END_POINT}/`, {
    params
});

const getPhotoDetails = (id) => httpClient.get(`${END_POINT}/${id}`);

const getMostLikedPhotos = () => httpClient.get(`${END_POINT}/`, {
    params: {
        order_by: "-like_count"
    }
});

const likePhoto = (id) => httpClient.post(`${END_POINT}/like/${id}/`);

const unlikePhoto = (id) => httpClient.delete(`${END_POINT}/like/${id}/`);


export {
    uploadPhoto,
    getUserPhotos,
    getFilteredPhotos,
    getPhotoDetails,
    getMostLikedPhotos,
    likePhoto,
    unlikePhoto
}