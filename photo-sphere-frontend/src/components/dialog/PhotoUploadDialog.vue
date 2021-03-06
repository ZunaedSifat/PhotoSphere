<template>
    <el-dialog
        v-model="dialog"
        title="Upload Photo"
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
            <el-form-item label="Image" prop="image">
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
                    <el-radio label="P">Public</el-radio>
                    <el-radio label="F">Followers</el-radio>
                    <el-radio label="O">Only me</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="Tags" prop="tags">
                <el-tag
                    :key="tag"
                    v-for="tag in form.tags"
                    closable
                    :disable-transitions="false"
                    @close="handleClose(tag)"
                >
                    {{ tag }}
                </el-tag>
                <el-autocomplete
                    style="
                        width: 90px !important;
                        margin-left: 10px !important;
                        vertical-align: bottom;
                    "
                    v-if="tagInputVisible"
                    v-model="tagInputValue"
                    ref="saveTagInput"
                    size="mini"
                    :fetch-suggestions="searchTag"
                    @select="handleSelect"
                    @keyup.enter="handleInputConfirm"
                >
                </el-autocomplete>
                <el-button
                    v-else
                    class="button-new-tag"
                    size="small"
                    @click="showInput"
                    >+ New Tag</el-button
                >
            </el-form-item>
            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 32px 16px"
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
import { createTag, getAllTags } from "@/api/tag.api";

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
            tags: [],
            fileList: [],
            file: null,
            tagInputVisible: false,
            tagInputValue: "",
            url: null,
            form: {
                image: "",
                title: "",
                caption: "",
                for_sale: false,
                price: 0,
                is_digital: false,
                privacy: null,
                tags: [],
                tagIds: [],
            },
            rules: {},
        };
    },
    methods: {
        createFilter(queryString) {
            return (tag) => {
                return (
                    tag.name
                        .toLowerCase()
                        .indexOf(queryString.toLowerCase()) === 0
                );
            };
        },
        searchTag(queryString, cb) {
            var results = queryString
                ? this.tags.filter(this.createFilter(queryString))
                : this.tags;
            // call callback function to return suggestions
            var res = results.map((result) => {
                return { value: result.name, id: result.id };
            });
            console.log(res);
            cb(res);
        },
        handleClose(tag) {
            this.form.tags.splice(this.form.tags.indexOf(tag), 1);
        },
        showInput() {
            this.tagInputVisible = true;
            // this.$nextTick((_) => {
            //     this.$refs.saveTagInput.$refs.input.focus();
            // });
        },
        async handleInputConfirm() {
            let inputValue = this.tagInputValue;
            if (inputValue) {
                const res = await createTag({
                    name: inputValue,
                    description: "lorem ipsum",
                });
                console.log(res.data);
                this.form.tags.push(res.data.name);
                this.form.tagIds.push(res.data.id);
            }
            this.tagInputVisible = false;
            this.tagInputValue = "";
        },
        handleSelect(tag) {
            this.form.tags.push(tag.value);
            this.form.tagIds.push(tag.id);
            console.log(this.form.tagIds);
            this.tagInputVisible = false;
            this.tagInputValue = "";
        },
        onClose(done) {
            this.$emit("close");
            done();
        },
        handleFileUpload() {
            this.form.image = this.$refs.file.files[0];
            this.url = URL.createObjectURL(this.form.image);
        },
        async onUpload() {
            this.loading = true;
            try {
                var finalTags = [];
                finalTags.push(...this.form.tagIds);

                var formData = new FormData();
                formData.append("title", this.form.title);
                formData.append("caption", this.form.caption);
                formData.append("for_sale", this.form.for_sale);
                formData.append("price", this.form.price);
                formData.append("is_digital", this.form.is_digital);
                for (let i = 0; i < finalTags.length; i++) {
                    formData.append("tags", finalTags[i]);
                }
                formData.append("image", this.form.image);

                const response = await uploadPhoto(formData);
                console.log(response);
                this.$emit("upload", response.data);
            } catch (error) {
                console.log(error.response);
            } finally {
                this.loading = false;
                this.$emit("close");
            }
        },
    },
    created() {
        getAllTags().then((res) => {
            this.tags.push(...res.data);
            console.log(this.tags);
        });
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