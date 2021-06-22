<template>
    <el-container>
        <el-row type="flex" style="margin-top: 8px">
            <el-col :span="12">
                <img class="bg__image" src="../../images/register_bg.jpg" />
            </el-col>
            <el-col :offset="3" :span="6">
                <el-form
                    ref="form"
                    :model="form"
                    :rules="rules"
                    size="small"
                    status-icon
                    style="margin-top: 80px"
                >
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
                            <el-button type="primary" circle>
                                <font-awesome-icon
                                    :icon="['fab', 'google']"
                                ></font-awesome-icon>
                            </el-button>
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
var emailValidator = require("email-validator");
export default {
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
            form: {
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
        onSubmit() {
            this.$refs.form.validate((valid) => {
                if (valid) {
                    alert("submit!");
                } else {
                    console.log("error submit!!");
                    return false;
                }
            });
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