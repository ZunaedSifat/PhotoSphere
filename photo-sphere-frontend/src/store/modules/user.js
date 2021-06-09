import {
    getOwnProfile,
    updateProfile
}
from '@/api/user.api';
import {
    RESET,
    SET_PROFILE
} from '@/store/mutation-types';

const initial_state = () => ({
    id: null,
    email: null,
    first_name: null,
    last_name: null,
    avatar: null,
});

const state = initial_state();

const getters = {
    getInitials(state) {
        if (state.first_name) {
            let initials = state.first_name.slice(0, 1);
            if (state.last_name) {
                initials = initials.concat(state.last_name.slice(0, 1));
            }
            return initials;
        }
        return '?';
    },
    getFullName(state) {
        if (state.first_name) {
            if (state.last_name) {
                return state.first_name + ' ' + state.last_name;
            } else {
                return state.first_name;
            }
        } else {
            return '';
        }
    },
    // isApproved(state) {
    //     return state.approval_status === 'A';
    // },
    // hasEnoughInfo(state) {
    //     return state.approval_status && state.approval_status !== 'N';
    // }
}

const actions = {
    async fetchCurrentUserProfile({ commit }) {
        try {
            const response = await getOwnProfile();
            commit(SET_PROFILE, response.data);
        } catch (error) {
            return Promise.reject(error);
        }
    },
    async updateCurrentUserProfile({ commit }, data) {
        try {
            const response = await updateProfile(data);
            commit(SET_PROFILE, response.data);
        } catch (error) {
            return Promise.reject(error);
        }
    }
}

const mutations = {
    [SET_PROFILE](state, profile) {
        console.log(profile);
        state = Object.assign(state, profile);
    },
    [RESET](state) {
        const new_state = initial_state();
        Object.keys(new_state).forEach(key => {
            state[key] = new_state[key];
        });
    }
};

export default {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
};