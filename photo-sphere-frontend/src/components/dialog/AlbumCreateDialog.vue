<template>
    <el-dialog
        v-model="dialog"
        title="Create New Album"
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
            <el-form-item label="Name" prop="name">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="Description" prop="description">
                <el-input
                    v-model="form.description"
                    type="textarea"
                    :rows="2"
                ></el-input>
            </el-form-item>
            <el-form-item label="Privacy" prop="privacy">
                <el-radio-group v-model="form.privacy">
                    <el-radio label="P">Public</el-radio>
                    <el-radio label="F">Followers</el-radio>
                    <el-radio label="O">Only me</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="Select Photos">
                <br />
                <el-space alignment="start" size="medium" wrap>
                    <el-card
                        v-for="(photo, index) in photos"
                        :key="index"
                        :photo="photo"
                        :body-style="{ padding: '0px', width: '100px' }"
                    >
                        <div style="position: relative">
                            <img :src="photo.image" class="image" />
                            <el-button
                                v-if="form.photoStatus[index]"
                                circle
                                type="primary"
                                icon="el-icon-check"
                                size="mini"
                                class="add-btn"
                                @click="deselectPhoto(index)"
                            ></el-button>
                            <el-button
                                v-else
                                circle
                                icon="el-icon-plus"
                                size="mini"
                                class="add-btn"
                                @click="selectPhoto(index)"
                            ></el-button>
                        </div>

                        <div style="padding-left: 8px; font-size: 0.8em">
                            <span>{{ photo.title }}</span>
                        </div>
                    </el-card>
                </el-space>
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
    name: "Album Create",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        photos: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            loading: false,
            fileList: [],
            file: null,
            form: {
                name: "",
                description: "",
                photoStatus: [],
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
        selectPhoto(index) {
            this.form.photoStatus[index] = true;
        },
        deselectPhoto(index) {
            this.form.photoStatus[index] = false;
        },
        async onCreate() {
            try {
                var selectedPhotos = [];
                for (let i = 0; i < this.photos.length; i++) {
                    if (this.form.photoStatus[i]) {
                        selectedPhotos.push(this.photos[i].id);
                    }
                }

                const data = {
                    name: this.form.name,
                    description: this.form.description,
                    photos: selectedPhotos,
                    privacy: this.form.privacy,
                };

                const response = await createAlbum(data);
                console.log(response);
                this.$emit("close");
            } catch (error) {
                console.log(error.response);
            }
        },
    },
    created() {
        this.photos.forEach((photo) => {
            this.form.photoStatus.push(false);
        });
    },
};
</script>

<style lang="scss" scoped>
.el-form-item {
    text-align: start;
}

.image {
    width: 100%;
    height: 80px;
    display: block;
}

.add-btn {
    position: absolute;
    top: 10%;
    right: 10%;
}
</style>