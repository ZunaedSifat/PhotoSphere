import httpClient from './httpClient';

const END_POINT = '/photo';

// used to fetch available info immediately after social signup
const getOwnProfile = () => httpClient.get(`${END_POINT}/me/`);

// used to fetch any public profile 
const getProfileById = (uuid) => httpClient.get(`${END_POINT}/${uuid}/`);

// used to update current user's profile information
const uploadPhoto = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

// used to fetch list of profiles
const getProfileList = (params) => httpClient.get(`${END_POINT}/`, {
    params
});

// used to search for profiles with given parameters
const searchProfile = (params) => httpClient.get(`${END_POINT}/search/`, {
    params
});

const getOwnPhotos = (user) => httpClient.get(`${END_POINT}/`, {
    params: {
        'user': user
    }
});

export {
    uploadPhoto,
    getOwnPhotos
}