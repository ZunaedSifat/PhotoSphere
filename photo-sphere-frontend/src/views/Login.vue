<template>
    <el-container>
        <el-row type="flex" style="margin-top: 8px">
            <el-col :span="12">
                <img
                    class="bg__image"
                    src="../../images/login_bg.jpg"
                    oncontextmenu="return false;"
                />
            </el-col>
            <el-col :offset="3" :span="6">
                <el-form
                    ref="form"
                    :model="form"
                    :rules="rules"
                    size="small"
                    status-icon
                    style="margin-top: 160px"
                >
                    <el-form-item label="E-mail" prop="email">
                        <el-input v-model="form.email"></el-input>
                    </el-form-item>
                    <el-form-item label="Password" prop="password">
                        <el-input
                            type="password"
                            v-model="form.password"
                        ></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button
                            type="primary"
                            style="padding: 8px 80px; margin-top: 16px"
                            :loading="loading"
                            @click="emailLogin"
                            >LOGIN
                        </el-button>
                    </el-form-item>

                    <el-form-item>
                        <el-row type="flex" justify="center">
                            <el-divider>OR</el-divider>
                        </el-row>
                        <el-row type="flex" justify="center">
                            <google-login
                                @socialClick="socialLogin"
                            ></google-login>

                            <el-button type="primary" circle>
                                <font-awesome-icon
                                    :icon="['fab', 'facebook']"
                                ></font-awesome-icon>
                            </el-button>
                        </el-row>
                    </el-form-item>
                </el-form>
            </el-col>
        </el-row>
    </el-container>
</template>

<script>
import GoogleLogin from "@/components/auth/GoogleLogin";
import authMixin from "@/mixins/authMixin";
var emailValidator = require("email-validator");

export default {
    components: {
        GoogleLogin,
    },
    mixins: [authMixin],
    data() {
        var validateEmail = (rule, value, callback) => {
            if (value === "") {
                callback(new Error("This field is required"));
            } else if (!emailValidator.validate(value)) {
                callback(new Error("Invalid e-mail address"));
            } else {
                callback();
            }
        };
        return {
            loading: false,
            form: {
                email: "",
                password: "",
            },
            rules: {
                email: [
                    {
                        required: true,
                        validator: validateEmail,
                        trigger: ["blur", "change"],
                    },
                ],
                password: [
                    {
                        required: true,
                        message: "This field is required",
                        trigger: ["blur", "change"],
                    },
                    {
                        min: 8,
                        message: "Password must be at least 8 characters",
                        trigger: ["blur", "change"],
                    },
                ],
            },
        };
    },
    methods: {
        changeRoute() {
            if (this.$route.params.nextUrl != null) {
                this.$router.replace(this.$route.params.nextUrl);
            } else {
                this.$router.replace({
                    name: "User-Profile",
                    params: { id: this.id },
                });
            }
        },
        async socialLogin(settings) {
            const params = {
                grant_type: "convert_token",
                client_id: process.env.VUE_APP_CLIENT_ID,
                client_secret: process.env.VUE_APP_CLIENT_SECRET,
                backend: settings.backend,
                token: settings.token,
            };
            try {
                await this.$store.dispatch("auth/exchangeSocialToken", params);
                await this.$store.dispatch("user/fetchCurrentUserProfile");
            } catch (error) {
                console.log(error);
            } finally {
                this.changeRoute();
            }
        },
        async emailLogin() {
            if (this.$refs.form.validate()) {
                this.loading = true;
                const params = {
                    grant_type: "password",
                    client_id: process.env.VUE_APP_CLIENT_ID,
                    client_secret: process.env.VUE_APP_CLIENT_SECRET,
                    username: this.form.email,
                    password: this.form.password,
                };
                try {
                    await this.$store.dispatch(
                        "auth/loginWithCredentials",
                        params
                    );
                    await this.$store.dispatch("user/fetchCurrentUserProfile");
                    this.changeRoute();
                } catch (error) {
                    this.loading = false;
                    console.log(error);
                }
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.bg__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.svg-inline--fa {
    font-size: 1.5em;
}
</style>