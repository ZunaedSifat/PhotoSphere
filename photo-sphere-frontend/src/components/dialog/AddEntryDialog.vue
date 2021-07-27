<template>
    <el-dialog
        v-model="dialog"
        title="Submit Entry to Exhibition"
        width="40%"
        show-close
        destroy-on-close
        :before-close="onClose"
    >
        <el-form ref="form" :model="form" size="small" status-icon>
            <template v-if="photosLoading">
                <div v-loading="photosLoading"></div>
            </template>
            <template v-else>
                <el-form-item label="Select Photo">
                    <br />
                    <el-space alignment="start" size="medium" wrap>
                        <el-card
                            v-for="(photo, index) in photos"
                            :key="index"
                            :photo="photo"
                            :body-style="{ padding: '0px', width: '100px' }"
                        >
                            <div style="position: relative">
                                <img
                                    :src="photo.image"
                                    class="image"
                                    oncontextmenu="return false;"
                                />
                                <el-button
                                    v-if="photoStatus[index]"
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
            </template>

            <el-form-item label="Order" prop="order">
                <el-input-number
                    :min="1"
                    v-model="form.order"
                ></el-input-number>
            </el-form-item>

            <el-form-item style="text-align: center">
                <el-button
                    type="primary"
                    style="padding: 8px 80px; margin: 24px 16px"
                    :loading="loading"
                    @click="onSubmit"
                    >SUBMIT
                </el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import authMixin from "@/mixins/authMixin";
import { getUserPhotos } from "@/api/photo.api";
import { createExhibitionEntry } from "@/api/exhibition.api";

export default {
    name: "Add entry",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        exhibition: {
            type: Number,
            required: true,
        },
    },
    mixins: [authMixin],
    data() {
        return {
            loading: false,
            form: {
                photo: null,
                order: null,
            },
            photos: [],
            photoStatus: [],
            photosLoading: false,
        };
    },
    methods: {
        onClose(done) {
            this.$emit("close");
            done();
        },
        selectPhoto(index) {
            for (let i = 0; i < this.photoStatus.length; i++) {
                this.photoStatus[i] = false;
            }
            this.photoStatus[index] = true;
            this.form.photo = this.photos[index].id;
        },
        deselectPhoto(index) {
            this.photoStatus[index] = false;
        },
        async onSubmit() {
            this.loading = true;
            try {
                const data = {
                    exhibition: this.exhibition,
                    photo: this.form.photo,
                    order: this.form.order,
                };

                const response = await createExhibitionEntry(data);
                console.log(response);
                this.$emit("add", response.data);
            } catch (error) {
                console.log(error.response);
            } finally {
                this.loading = false;
                this.$emit("close");
            }
        },
    },
    created() {
        this.photosLoading = true;
        getUserPhotos(this.id)
            .then((res) => {
                this.photos.push(...res.data);
                this.photosLoading = false;
                console.log(this.photos);
                this.photos.forEach((photo) => {
                    this.photoStatus.push(false);
                });
            })
            .catch((error) => {
                console.log(error);
                this.photosLoading = false;
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