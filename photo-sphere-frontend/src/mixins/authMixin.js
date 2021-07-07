import { mapState, mapGetters } from "vuex";

const authMixin = {
    computed: {
        ...mapState("user", ["id", "avatar"]),
        ...mapGetters("auth", ["isLoggedIn"]),
        ...mapGetters("user", ["getFullName", "getInitials"]),
    },
    methods: {
        logOut() {
            this.$store.dispatch("auth/logOut");
            this.$router.push("/");
        }
    }
};

export default authMixin;