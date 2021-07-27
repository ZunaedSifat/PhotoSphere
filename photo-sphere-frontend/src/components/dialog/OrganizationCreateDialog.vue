<template>
    <el-dialog
        v-model="dialog"
        title="Create New Organization"
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
                </div>
            </el-form-item>

            <el-form-item label="Name" prop="name">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="Description" prop="description">
                <el-input
                    v-model="form.description"
                    type="textarea"
                    :rows="3"
                ></el-input>
            </el-form-item>
            <el-form-item label="Website" prop="website">
                <el-input v-model="form.website"></el-input>
            </el-form-item>
            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 32px 16px"
                    :loading="loading"
                    @click="onCreate"
                    >CREATE ORGANIZATION
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { createOrganization } from "@/api/organization.api";

export default {
    name: "Create organization",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            loading: false,
            url: null,
            form: {
                avatar: null,
                name: "",
                description: "",
                website: "",
            },
            rules: {},
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
        async onCreate() {
            this.loading = true;
            try {
                var formData = new FormData();
                formData.append("name", this.form.name);
                formData.append("description", this.form.description);
                formData.append("website", this.form.website);
                formData.append("avatar", this.form.avatar);

                const response = await createOrganization(formData);
                console.log(response);
                this.$emit("create", response.data);
            } catch (error) {
                console.log(error.response);
            } finally {
                this.loading = false;
                this.$emit("close");
            }
        },
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