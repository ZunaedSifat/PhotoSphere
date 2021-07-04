<template>
    <el-dialog
        v-model="dialog"
        title="Upload Photo"
        width="40%"
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
            <input
                type="file"
                id="file"
                ref="file"
                class="input is-rounded"
                @change="handleFileUpload"
            />
            <img v-if="file" :src="file.url" />
            <!-- <el-upload
                drag
                thumbnail-mode
                action="https://jsonplaceholder.typicode.com/posts/"
                :auto-upload="false"
                :on-success="onFileLoad"
                :file-list="fileList"
                list-type="picture"
                style="margin-bottom: 16px"
            >
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">
                    Drop file here or <em>click to upload</em>
                </div>
                <template #tip>
                    <div class="el-upload__tip">
                        jpg/png files with a size less than 500kb
                    </div>
                </template>
            </el-upload> -->
            <el-form-item label="Title" prop="title">
                <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="Caption" prop="caption">
                <el-input
                    v-model="form.caption"
                    type="textarea"
                    :rows="2"
                ></el-input>
            </el-form-item>
            <el-form-item prop="for_sale">
                <el-checkbox
                    v-model="form.for_sale"
                    label="This photo is for sale"
                ></el-checkbox>
            </el-form-item>
            <el-form-item label="Price" prop="price">
                <el-input-number
                    v-model="form.price"
                    :disabled="!form.for_sale"
                ></el-input-number>
            </el-form-item>
            <el-form-item prop="is_digital">
                <el-checkbox
                    v-model="form.is_digital"
                    label="This photo is digital only [no physical frame available]"
                ></el-checkbox>
            </el-form-item>
            <el-form-item label="Privacy" prop="privacy">
                <el-radio-group v-model="form.privacy">
                    <el-radio label="Public"></el-radio>
                    <el-radio label="Followers"></el-radio>
                    <el-radio label="Only me"></el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 16px"
                    :loading="loading"
                    @click="onUpload"
                    >UPLOAD
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import { uploadPhoto } from "@/api/photo.api";

export default {
    name: "Photo upload",
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
                image: "",
                title: "",
                caption: "",
                for_sale: false,
                price: 0,
                is_digital: false,
                privacy: null,
            },
            rules: {},
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },
        onFileLoad(response, file, fileList) {
            var newFile = {
                name: file.name,
                url: file.url,
            };
            Vue.set(this.fileList, 0, newFile);
            this.image = file;
        },
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
        },
        async onUpload() {
            try {
                var formData = new FormData();
                formData.append("title", this.form.title);
                formData.append("caption", this.form.caption);
                formData.append("for_sale", this.form.for_sale);
                formData.append("price", this.form.price);
                formData.append("is_digital", this.form.is_digital);
                formData.append("image", this.file);

                var data = {
                    title: this.form.title,
                    caption: this.form.caption,
                    image: this.form.image,
                    for_sale: this.form.for_sale,
                    price: this.form.price,
                    is_digital: this.form.is_digital,
                };

                const response = await uploadPhoto(formData);
                console.log(response);
                this.$emit("close");
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