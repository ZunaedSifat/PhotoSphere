<template>
    <el-container style="margin: 32px 0px">
        <el-row type="flex">
            <el-col :span="6">
                <el-avatar fit="fill" :size="160" style="margin: 16px 0px">
                    <img src="../../images/profile.jpg" />
                </el-avatar>
                <el-container style="justify-content: center">
                    <span>{{ getFullName }}</span>
                </el-container>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
            <el-col :span="12" style="justify-content: start">
                <el-row type="flex" align="middle">
                    <h3>Photos</h3>
                    <el-button
                        size="mini"
                        icon="el-icon-upload2"
                        @click="photoUpload = true"
                        @close="photoUpload = false"
                        >Upload new photo</el-button
                    >
                </el-row>

                <el-row type="flex" align="middle">
                    <h3>Albums</h3>
                    <el-button size="mini" icon="el-icon-folder-add"
                        >Create new album</el-button
                    >
                </el-row>
            </el-col>
            <el-col :span="1">
                <el-divider direction="vertical"></el-divider>
            </el-col>
        </el-row>
        <photo-upload-dialog :dialog="photoUpload"></photo-upload-dialog>
    </el-container>
</template>

<script>
import authMixin from "@/mixins/authMixin";
import PhotoUploadDialog from "@/components/dialog/PhotoUploadDialog";

export default {
    mixins: [authMixin],
    components: {
        PhotoUploadDialog,
    },
    data() {
        return {
            photoUpload: false,
        };
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