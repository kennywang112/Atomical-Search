#!/bin/bash

# 并发函数
query_range() {
    local start=$1
    local end=$2
    local file="res_$start-$end.log"

    for (( i=start; i<=end; i++ ))
    do
        formatted_number=$(printf "%04d" $i)
        yarn cli get-container-item "#toothy" "$formatted_number" >> $file
    done
}

# 初始化参数
start=1
end=10000
step=1000

# 并发执行
for (( i=start; i<=end; i+=step ))
do
    next=$((i + step - 1))
    if [ $next -gt $end ]; then
        next=$end
    fi

    query_range $i $next &  # 在后台执行
done

wait  # 等待所有后台任务完成

# 合并所有结果到一个文件
cat res_*.log > res.log
#rm res_*.log  # 删除临时文件

echo "查询完成，结果已输出到 res.log"