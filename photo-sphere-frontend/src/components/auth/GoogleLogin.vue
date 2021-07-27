<template>
    <el-button type="primary" circle @click="onClick">
        <font-awesome-icon :icon="['fab', 'google']"></font-awesome-icon>
    </el-button>
</template>

<script>
export default {
    // props: {
    //     signup: {
    //         type: Boolean,
    //         default: false,
    //     },
    // },

    data() {
        return {
            params: {
                client_id: process.env.VUE_APP_GOOGLE_OAUTH_CLIENT_ID,
            },
        };
    },
    methods: {
        async onClick() {
            try {
                const user = await this.$gAuth.signIn();
                console.log(user);
                this.onSuccess(user);
            } catch (error) {
                this.onFailure(error);
            }
        },
        onSuccess(user) {
            const accessToken = user.Zb.access_token;
            const settings = {
                backend: "google-oauth2",
                token: accessToken,
            };
            this.$emit("socialClick", settings);
        },
        onFailure(errorData) {
            // The errorData variable contains failure details
            console.log(errorData);
        },
    },
};
</script>

<style lang="scss" scoped>
svg {
    font-size: 16px;
}
</style>