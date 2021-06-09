import Vuex from 'vuex';
import auth from './modules/auth';


const store = new Vuex.Store({
    modules: {
        auth,
    },
    strict: process.env.NODE_ENV !== 'production'
});

export default store;