<template>
    <el-dialog
        v-model="dialog"
        title="Share Photo"
        width="50%"
        show-close
        destroy-on-close
        :before-close="onClose"
    >
        <div style="text-align: center">
            <p>{{ getFullURL() }}</p>
            <img :src="photoURL" class="image" oncontextmenu="return false;" />
        </div>

        <facebook-button :picture="photoURL" />
        <twitter-button :picture="photoURL" />
        <tumblr-button :picture="photoURL" />
        <pinterest-button :picture="photoURL" />
    </el-dialog>
</template>

<script>
export default {
    name: "Share photo",
    props: {
        dialog: {
            type: Boolean,
            default: false,
        },
        photoURL: {
            required: true,
        },
    },
    methods: {
        getFullURL() {
            return window.location.origin + this.$route.path;
        },
        onClose(done) {
            this.$emit("close");
            done();
        },
    },
};
</script>

<style lang="scss" scoped>
.image {
    width: 30%;
    margin-bottom: 20px;
}
</style>