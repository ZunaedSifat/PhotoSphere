
<template>
    <el-card
        shadow="hover"
        :body-style="{ padding: '0px', width: '200px' }"
        @click="viewDetails"
    >
        <img :src="photo.image" class="image" oncontextmenu="return false;" />
        <div style="padding: 14px">
            <span>{{ photo.title }}</span>
        </div>
    </el-card>
</template>

<script>
export default {
    props: {
        photo: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            currentDate: new Date(),
        };
    },
    methods: {
        viewDetails() {
            this.$router.push({
                name: "Photo-Details",
                params: { id: this.photo.id },
            });
        },
    },
};
</script>

<style lang="scss" scoped>
.time {
    font-size: 13px;
    color: #999;
}

.bottom {
    margin-top: 13px;
    line-height: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.button {
    padding: 0;
    min-height: auto;
}

.image {
    width: 100%;
    height: 120px;
    display: block;
}

.el-card:hover {
    cursor: pointer;
}

.el-card.is-hover-shadow:hover,
.el-card.is-hover-shadow:focus {
    box-shadow: 4px 4px 12px 0 rgb(0 0 0 / 20%);
}
</style>
