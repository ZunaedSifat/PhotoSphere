<template>
    <el-dialog
        v-model="dialog"
        title="Edit Profile"
        width="40%"
        show-close
        destroy-on-close
        :before-close="onClose"
    >
        <el-form
            enctype="multipart/form-data"
            ref="form"
            :model="form"
            :rules="rules"
            size="small"
            status-icon
        >
            <el-form-item label="Avatar" prop="avatar">
                <input
                    type="file"
                    id="file"
                    ref="file"
                    class="input is-rounded"
                    @change="handleFileUpload"
                />
                <div>
                    <img
                        class="image-preview"
                        v-if="url"
                        :src="url"
                        oncontextmenu="return false;"
                    />
                    <img
                        class="image-preview"
                        v-else-if="form.avatar"
                        :src="form.avatar"
                        oncontextmenu="return false;"
                    />
                </div>
            </el-form-item>

            <el-form-item label="First Name" prop="first_name">
                <el-input v-model="form.first_name"></el-input>
            </el-form-item>
            <el-form-item label="Last Name" prop="last_name">
                <el-input v-model="form.last_name"></el-input>
            </el-form-item>

            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin-top: 16px"
                    :loading="loading"
                    @click="onSubmit"
                    >SAVE
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { updateProfile } from "@/api/user.api";

export default {
    name: "Edit Profile",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        profile: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
            url: null,
            form: {
                avatar: null,
                first_name: "",
                last_name: "",
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
            },
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },
        handleFileUpload() {
            this.form.avatar = this.$refs.file.files[0];
            this.url = URL.createObjectURL(this.form.avatar);
        },
        async onSubmit() {
            if (this.$refs.form.validate()) {
                this.loading = true;
                var formData = new FormData();
                formData.append("first_name", this.form.first_name);
                formData.append("last_name", this.form.last_name);
                if (this.url) {
                    formData.append("avatar", this.form.avatar);
                }
                try {
                    const response = await updateProfile(formData);
                    console.log(response);
                    await this.$store.dispatch("user/fetchCurrentUserProfile");
                    this.$emit("edit", response.data);
                } catch (error) {
                    console.log(error.response);
                } finally {
                    this.loading = false;
                    this.$emit("close");
                }
            }
        },
    },
    created() {
        this.form.avatar = this.profile.avatar;
        this.form.first_name = this.profile.first_name;
        this.form.last_name = this.profile.last_name;
        this.form.email = this.profile.email;
    },
};
</script>

<style lang="scss" scoped>
.el-form-item {
    text-align: start;
}

.el-tag + .el-tag {
    margin-left: 10px;
}
.button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
}

.image-preview {
    border: 1px solid grey;
    border-radius: 8px;
    padding: 8px;
    margin-top: 4px;
    width: 100px;
    height: 100px;
}
</style>