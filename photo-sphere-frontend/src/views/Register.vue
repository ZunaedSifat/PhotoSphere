<template>
    <el-container>
        <el-row type="flex" style="margin-top: 8px">
            <el-col :span="12">
                <img
                    class="bg__image"
                    src="../../images/register_bg.jpg"
                    oncontextmenu="return false;"
                />
            </el-col>
            <el-col :offset="3" :span="6">
                <el-form
                    enctype="multipart/form-data"
                    ref="form"
                    :model="form"
                    :rules="rules"
                    size="small"
                    status-icon
                    style="margin-top: 80px"
                >
                    <el-form-item label="Avatar" prop="avatar">
                        <input
                            type="file"
                            id="avatar"
                            ref="file"
                            class="input is-rounded"
                            @change="handleFileUpload"
                    /></el-form-item>
                    <el-form-item label="First Name" prop="first_name">
                        <el-input v-model="form.first_name"></el-input>
                    </el-form-item>
                    <el-form-item label="Last Name" prop="last_name">
                        <el-input v-model="form.last_name"></el-input>
                    </el-form-item>
                    <el-form-item label="E-mail" prop="email">
                        <el-input v-model="form.email"></el-input>
                    </el-form-item>
                    <el-form-item label="Password" prop="password">
                        <el-input
                            type="password"
                            v-model="form.password"
                        ></el-input>
                    </el-form-item>
                    <el-form-item
                        label="Confirm Password"
                        prop="confirmPassword"
                    >
                        <el-input
                            type="password"
                            v-model="form.confirmPassword"
                        ></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button
                            type="primary"
                            style="padding: 8px 80px; margin-top: 16px"
                            @click="onSubmit"
                            >REGISTER
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
var emailValidator = require("email-validator");
import { createProfile } from "@/api/user.api";
import authMixin from "@/mixins/authMixin";

export default {
    mixins: [authMixin],
    components: {
        GoogleLogin,
    },
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

        var validateConfirmPassword = (rule, value, callback) => {
            if (value === "") {
                callback(new Error("This field is required"));
            } else if (value !== this.form.password) {
                callback(new Error("Passwords don't match"));
            } else {
                callback();
            }
        };
        return {
            loading: false,
            form: {
                avatar: null,
                first_name: "",
                last_name: "",
                email: "",
                password: "",
                confirmPassword: "",
            },
            rules: {
                first_name: [
                    {
                        required: true,
                        message: "This field is required",
                        trigger: ["blur", "change"],
                    },
                ],
                last_name: [
                    {
                        required: true,
                        message: "This field is required",
                        trigger: ["blur", "change"],
                    },
                ],
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
                confirmPassword: [
                    {
                        required: true,
                        validator: validateConfirmPassword,
                        trigger: ["blur", "change"],
                    },
                ],
            },
        };
    },
    methods: {
        handleFileUpload() {
            this.form.avatar = this.$refs.file.files[0];
        },
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
        async onSubmit() {
            if (this.$refs.form.validate()) {
                this.loading = true;
                var formData = new FormData();
                formData.append("first_name", this.form.first_name);
                formData.append("last_name", this.form.last_name);
                formData.append("email", this.form.email);
                formData.append("password", this.form.password);
                if (this.form.avatar) {
                    formData.append("avatar", this.form.avatar);
                }

                try {
                    await createProfile(formData);
                    await this.$store.dispatch("user/fetchCurrentUserProfile");
                } catch (error) {
                    this.loading = false;
                    console.log(error.response);
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