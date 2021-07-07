<template>
    <el-dialog
        v-model="dialog"
        title="Create New Exhibition"
        width="60%"
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
            <el-form-item label="Submission Fee" prop="submissionFee">
                <el-input-number v-model="form.submissionFee"></el-input-number>
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
import { createAlbum } from "@/api/album.api";

export default {
    name: "Exhibition Create",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            loading: false,
            fileList: [],
            file: null,
            form: {
                title: "",
                description: "",
                date: null,
                startDate: null,
                endDate: null,
                entryFee: 0,
                submissionFee: 0,
                privacy: null,
                theme: null,
            },
            rules: {},
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },

        async onCreate() {
            try {
                var data = {
                    title: this.form.title,
                    description: this.form.description,
                    privacy: this.form.privacy,
                };

                console.log(this.form.date[0]);
                console.log(this.form.date[1]);

                // const response = await createAlbum(data);
                // console.log(response);
                // this.$emit("close");
            } catch (error) {
                console.log(error.response);
            } finally {
                console.log("done");
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
</style>