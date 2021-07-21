import httpClient from './httpClient';

const END_POINT = '/user';

const createProfile = (data) => httpClient.post(`${END_POINT}/`, data, {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
    },
});

// used to fetch available info immediately after social signup
const getOwnProfile = () => httpClient.get(`${END_POINT}/me/`);

// used to fetch any public profile 
const getProfileById = (id) => httpClient.get(`${END_POINT}/${id}/`);

// used to update current user's profile information
const updateProfile = (data) => httpClient.patch(`${END_POINT}/me/`, data);

// used to fetch list of profiles
const getProfileList = (params) => httpClient.get(`${END_POINT}/`, {
    params
});

// used to search for profiles with given parameters
const searchProfile = (params) => httpClient.get(`${END_POINT}/search/`, {
    params
});

export {
    createProfile,
    getOwnProfile,
    getProfileById,
    updateProfile,
    getProfileList,
    searchProfile
}