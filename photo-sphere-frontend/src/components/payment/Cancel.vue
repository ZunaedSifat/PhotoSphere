<template>
    <el-container style="margin: 60px 0px; text-align: center">
        <el-row type="flex">
            <el-col :offset="6" :span="12">
                <img
                    src="../../../images/cancel.png"
                    :width="100"
                    :height="100"
                />

                <h2 style="color: indianred">Payment Canceled</h2>
                <br /><br />
                <template v-if="loading">
                    <div v-loading="loading"></div>
                </template>
                <template v-else>
                    <el-descriptions :column="1" border title="Order Details">
                        <el-descriptions-item label="Address">
                            {{ order.address }}
                        </el-descriptions-item>
                        <el-descriptions-item label="City">
                            {{ order.city }}
                        </el-descriptions-item>
                        <el-descriptions-item label="Phone">
                            {{ order.phone }}
                        </el-descriptions-item>
                        <el-descriptions-item label="Transaction ID">
                            {{ order.transaction_id }}
                        </el-descriptions-item>
                    </el-descriptions>
                </template>
                <p style="margin-top: 32px">
                    You can close this window and continue
                </p>
            </el-col>
        </el-row>
    </el-container>
</template>

<script>
import { getOrder } from "@/api/order.api";

export default {
    data() {
        return {
            id: this.$route.params.id,
            loading: false,
            order: null,
        };
    },
    created() {
        this.loading = true;
        getOrder(this.id)
            .then((res) => {
                this.order = res.data;
                this.loading = false;
                console.log(this.order);
            })
            .catch((error) => {
                console.log(error);
                this.loading = false;
            });
    },
};
</script>

