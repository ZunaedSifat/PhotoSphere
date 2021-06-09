import { mapState, mapGetters } from "vuex";

const authMixin = {
    computed: {
        ...mapState("profile", ["uuid", "has_approval_permission"]),
        ...mapGetters("auth", ["isLoggedIn"]),
        ...mapGetters("profile", ["getFullName", "getInitials", "isApproved", "hasEnoughInfo"]),
    },
    methods: {
        logOut() {
            this.$store.dispatch("auth/logOut");
            this.$router.push("/");
        }
    }
};

export default authMixin;