<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :span="6">
                <template v-if="loading">
                    <div v-loading="loading"></div>
                </template>
                <template v-else>
                    <el-avatar fit="fill" :size="160" style="margin: 16px 0px">
                        <img
                            v-if="profile.avatar"
                            :src="profile.avatar"
                            oncontextmenu="return false;"
                        />

                        <img
                            v-else
                            src="../../images/profile.jpg"
                            oncontextmenu="return false;"
                        />
                    </el-avatar>
                    <el-container style="justify-content: center">
                        <span>{{
                            profile.first_name + " " + profile.last_name
                        }}</span>
                    </el-container>
                    <br />
                    <el-button
                        v-if="isCurrentUser"
                        type="primary"
                        style="padding: 0px 80px"
                        @click="profileEdit = true"
                        >Edit Profile</el-button
                    >
                </template>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :span="12" style="justify-content: start">
                <el-row type="flex" align="middle">
                    <h3>Photos</h3>
                    <el-button
                        v-if="isCurrentUser"
                        size="mini"
                        icon="el-icon-upload2"
                        @click="photoUpload = true"
                        @close="photoUpload = false"
                        >Upload new photo</el-button
                    >
                </el-row>

                <template v-if="photosLoading">
                    <div v-loading="photosLoading"></div>
                </template>
                <template v-else>
                    <el-space alignment="start" size="medium" wrap>
                        <photo-preview-card
                            v-for="(photo, index) in photos"
                            :key="index"
                            :photo="photo"
                        ></photo-preview-card>
                    </el-space>
                </template>

                <el-row type="flex" align="middle">
                    <h3>Albums</h3>
                    <el-button
                        v-if="isCurrentUser"
                        size="mini"
                        icon="el-icon-folder-add"
                        @click="albumCreate = true"
                        @close="albumCreate = false"
                        >Create new album</el-button
                    >
                </el-row>

                <template v-if="albumsLoading">
                    <div v-loading="albumsLoading"></div>
                </template>
                <template v-else>
                    <el-space alignment="start" size="medium" wrap>
                        <album-preview-card
                            v-for="(album, index) in albums"
                            :key="index"
                            :album="album"
                        ></album-preview-card>
                    </el-space>
                </template>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
        </el-row>
        <edit-profile-dialog
            v-if="profile"
            :dialog="profileEdit"
            :profile="profile"
            @edit="updateProfile"
            @close="profileEdit = false"
        ></edit-profile-dialog>
        <photo-upload-dialog
            :dialog="photoUpload"
            @upload="addNewPhoto"
            @close="photoUpload = false"
        ></photo-upload-dialog>
        <album-create-dialog
            v-if="photos.length != 0"
            :dialog="albumCreate"
            :photos="photos"
            @create="addNewAlbum"
            @close="albumCreate = false"
        ></album-create-dialog>
        <el-dialog v-else title="Unable to create album"
            >Please upload some photos first</el-dialog
        >
    </el-container>
</template>

<script>
import authMixin from "@/mixins/authMixin";
import PhotoUploadDialog from "@/components/dialog/PhotoUploadDialog";
import PhotoPreviewCard from "@/components/photo/PhotoPreviewCard";
import AlbumPreviewCard from "@/components/photo/AlbumPreviewCard";
import { getProfileById } from "@/api/user.api";
import { getUserPhotos } from "@/api/photo.api";
import { getUserAlbums } from "@/api/album.api";
import AlbumCreateDialog from "@/components/dialog/AlbumCreateDialog.vue";
import EditProfileDialog from "@/components/dialog/EditProfileDialog.vue";

export default {
    mixins: [authMixin],
    components: {
        PhotoUploadDialog,
        PhotoPreviewCard,
        AlbumPreviewCard,
        AlbumCreateDialog,
        EditProfileDialog,
    },
    data() {
        return {
            loading: true,
            profile: null,
            profileEdit: false,
            photoUpload: false,
            albumCreate: false,
            photosLoading: true,
            albumsLoading: true,
            photos: [],
            albums: [],
        };
    },
    computed: {
        isCurrentUser() {
            return this.id == this.$route.params.id;
        },
    },
    methods: {
        addNewPhoto(photo) {
            this.photos.push(photo);
        },
        addNewAlbum(album) {
            this.albums.push(album);
        },
        updateProfile(newProfile) {
            this.profile.first_name = newProfile.first_name;
            this.profile.last_name = newProfile.last_name;
            this.profile.avatar = newProfile.avatar;
            console.log("goru");
            console.log(newProfile);
        },
    },
    created() {
        this.loading = true;
        getProfileById(this.$route.params.id)
            .then((res) => {
                console.log(res);
                this.profile = res.data;
            })
            .catch((error) => console.log(error))
            .finally(() => (this.loading = false));

        this.photosLoading = true;
        getUserPhotos(this.$route.params.id)
            .then((res) => {
                console.log(res);
                this.photos = res.data;
            })
            .catch((error) => console.log(error))
            .finally(() => (this.photosLoading = false));

        this.albumsLoading = true;
        getUserAlbums(this.$route.params.id)
            .then((res) => {
                console.log(res);
                this.albums = res.data;
            })
            .catch((error) => console.log(error))
            .finally(() => (this.albumsLoading = false));
    },
};
</script>

<style lang="scss" scoped>
.el-divider--vertical {
    height: 20em !important;
}

h3 {
    text-align: start;
    margin-right: 16px;
}

// .el-button {
//     padding: 8px !important;
//     height: 32px !important;
// }
</style>