// 选择工作类型、地理位置
// $(function () {
//     page_all = 1; // 设置默认值
//     page_size = 10; //默认页面大小
//     page_cur = 1; // 默认当前页面
//     // 进入页面即运行
//     var category = "全部"
//     var type = "不限"
//     var workplace = "不限"
//     get_request()
//
//     // 监听点击事件
//     $(".job-category :radio").on("click", get_category);
//     $(".job-type :radio").on("click", get_type);
//     $(".workplace :radio").on("click", get_workplace);
//
//     function get_category() {
//         category = $(this).val()
//         get_request()
//     }
//
//     function get_type() {
//         type = $(this).val()
//         get_request();
//     }
//
//     function get_workplace() {
//         workplace = $(this).val();
//         get_request();
//     }
//
//     // 异步请求
//     function get_request() {
//         $.ajax({
//             url: '/seeker/index/',// 跳转到 action
//             data: {
//                 "category": category,
//                 "type": type,
//                 "workplace": workplace,
//             },
//             type: 'post',
//             cache: false,
//             dataType: 'json',
//             success: function (response) {
//                 // 1.1 把ajax返回的数据放到table中
//                 // 1.2 至此所有数据都在table中一页显示 console.log(tbody.innerHTML);
//                 data =  response.data // 返回列表
//                 for (var i = 0; i < data.length; ++i) {
//                     var dom = document.createElement("tr");
//                     dom.innerHTML =
//                         "<td>"+"<a href='url'>".replace('url','{{ url_for(\'auth.login\') }}') + data[i].job_name + "</a></td>" +
//                         "<td>" + data[i].job_category + "</td>" +
//                         "<td>" + data[i].workplace + "</td>" +
//                         "<td>" + data[i].post_time + "</td>"
//                     // let url = `{{ url_for('auth.login') }}`;
//                     // document.getElementById("url").href = url;
//                     document.getElementById("tbody").appendChild(dom);
//                 }
//
//                 // 1.2 把所有的tr元素保存到数组中
//                 var trs = $("#tbody tr"); // 获取所有的tr，即行元素
//                 arr_tr = new Array(trs.length); //创建数组
//                 for (var i = 0; i < arr_tr.length; ++i) {
//                     arr_tr[i] = trs[i].innerHTML; //数组的每一项都是tr的内容（带td标签标签,不含tr标签）
//                     // console.log(trs[i].innerHTML);
//                 }
//
//
//                 // 1.3 在给定page_size的情况下，计算总的缓存页面数
//                 if (arr_tr.length % page_size == 0) {
//                     page_all = arr_tr.length / page_size;
//                 } else {
//                     page_all = parseInt(arr_tr.length / page_size) + 1;
//                 }
//                 // 1.4 跳转到具体页面
//                 jump(page_cur);
//
//             }, // end of success
//             error: function (data, status) {
//
//             }
//         }); // end of ajax
//     } // end of get_request()
// }) // end of entrance

// 2. 自定义跳转函数
function jump(tar) {
    empty_page = false;
    //2.1 设置局部变量的值，并做越界处理
    p_cur = tar

    if (tar < 1) { // 如果目标跳转页面小于1，则目标跳转页面设置为1，同时把当前页面设置为1
        p_cur = 1;
    }
    if (tar > page_all) { // 如果目标页超出最大页面，设置威最大页面
        p_cur = page_all;
    }

    // 2.2 清空上面tbody设置的表格，为加载指定页面做准备
    $("#tbody").html("");

    // 2.3 动态创建 page_cur的内容，插入tbody中
    for (var i = 0; i < page_size; ++i) {
        //提前判断下一个元素，超出范围跳出
        if (arr_tr[(p_cur - 1) * page_size + i] == null) {
            if (p_cur == 1 && i == 0) {
                console.log("i = " + i);
                empty_page = true; // 判断是否是空页
            }
            break;
        }
        var div = document.createElement("tr");
        div.innerHTML = arr_tr[(p_cur - 1) * page_size + i]; // arr_tr中都是 <td>xx</td>
        document.getElementById("tbody").appendChild(div);//加入tbody中 // $("#tbody").append(div);
    }
    pagination_dom.innerHTML = ""; // 一定要清空子元素，防止上次加载的结果留下

    if (empty_page == true) {
        $("#no-data span").css("display", "block");
        prev();
        next();
    } else {
        $("#no-data span").css("display", "none");
        prev();
        iter_pages(p_cur);
        next();
    }
}

// 选择性页面加载 page 1,2,3...10,11,12
function iter_pages(p_cur) {
    var left_edge = 2;
    var left_current = 3;
    var right_current = 5;
    var right_edge = 2
    var last = 0
    for (var num = 1; num <= page_all; ++num) {
        var dom = document.createElement('li');
        if ((num <= left_edge) || ((num > p_cur - left_current - 1) && (num < p_cur + right_current))
            || (num > page_all - right_edge)) {
            if (last + 1 != num) {
                var dom = document.createElement('li');
                dom.className = 'page-item'
                var element = "<a class=\"page-link\">...</a>"
                dom.innerHTML = element;
                pagination_dom.appendChild(dom);
            } else {
                if (num == p_cur) {
                    dom.className = 'page-item active'
                    var element = "<a class=\"page-link\"  onClick='jump(" + num + ")'>" + num + "</a>"
                } else {
                    dom.className = 'page-item'
                    var element = "<a class=\"page-link\"  onClick='jump(" + num + ")'>" + num + "</a>"
                }
                dom.innerHTML = element;
                pagination_dom.appendChild(dom);
            }
            last = num
        }

    }
}

// Previous
function prev() {
    // 2.4 设置底部页码导航标签 - 上一页
    var dom = document.createElement('li')
    dom.className = 'page-item'
    var element = "<a class=\"page-link\" onClick=\"jump(--p_cur)\" tabindex=\"-1\" aria-disabled=\"true\">Previous</a>"
    dom.innerHTML = element;
    pagination_dom.appendChild(dom);
}

//Next
function next() {
    // 2.6 设置底部页码导航标签 - 下一页
    var dom = document.createElement('li')
    dom.className = 'page-item'
    var element = '<li class="page-item"><a class="page-link" onClick="jump(++p_cur)">Next</a></li>'
    dom.innerHTML = element;
    pagination_dom.appendChild(dom);
}
