<template>
    <el-dialog
        v-model="dialog"
        title="Create New Exhibition"
        width="50%"
        show-close
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
            <el-form-item label="Cover Photo" prop="avatar">
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

            <el-form-item label="Title" prop="title">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="Description" prop="description">
                <el-input
                    v-model="form.description"
                    type="textarea"
                    autosize
                    :rows="2"
                ></el-input>
            </el-form-item>
            <el-form-item label="Date"
                ><div class="block">
                    <el-date-picker
                        v-model="form.date"
                        type="daterange"
                        unlink-panels
                        range-separator="To"
                        start-placeholder="Start date"
                        end-placeholder="End date"
                    >
                    </el-date-picker></div
            ></el-form-item>
            <el-form-item label="Entry Fee" prop="entryFee">
                <el-input-number v-model="form.entryFee"></el-input-number>
            </el-form-item>
            <el-form-item label="Privacy" prop="privacy">
                <el-radio-group v-model="form.privacy">
                    <el-radio label="P">Public</el-radio>
                    <el-radio label="F">Followers</el-radio>
                    <el-radio label="O">Only me</el-radio>
                </el-radio-group>
            </el-form-item>

            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 16px"
                    :loading="loading"
                    @click="onCreate"
                    >CREATE
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { createExhibition } from "@/api/exhibition.api";

export default {
    name: "Exhibition Create",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        organization: {
            type: Number,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
            url: null,
            form: {
                avatar: null,
                title: "",
                description: "",
                startDate: null,
                endDate: null,
                entryFee: 0,
                privacy: null,
                theme: null,
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
        async onCreate() {
            this.loading = true;
            try {
                var formData = new FormData();
                formData.append("organizer", this.organization);
                formData.append("title", this.form.title);
                formData.append("description", this.form.description);
                formData.append("entry_fee", this.form.entryFee);
                formData.append(
                    "start_date",
                    new Date(this.form.startDate).toISOString()
                );
                formData.append(
                    "end_date",
                    new Date(this.form.endDate).toISOString()
                );
                if (this.form.avatar) {
                    formData.append("avatar", this.form.avatar);
                }

                const response = await createExhibition(formData);
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

.image-preview {
    border: 1px solid grey;
    border-radius: 8px;
    padding: 8px;
    margin-top: 4px;
    width: 100px;
    height: 100px;
}
</style>