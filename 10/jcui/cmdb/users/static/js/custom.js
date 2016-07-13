/**
 * Created by op on 16-7-5.
 */
jQuery(document).ready(function () {
        // 分页展示
        $('table').DataTable({
            "language": {
                "processing": "处理中...",
                "lengthMenu": "显示 _MENU_ 项结果",
                "zeroRecords": "没有匹配结果",
                "info": "显示第 _START_ 至 _END_ 项结果，共 _TOTAL_ 项",
                "infoEmpty": "显示第 0 至 0 项结果，共 0 项",
                "infoFiltered": "(由 _MAX_ 项结果过滤)",
                "infoPostFix": "",
                "search": "搜索:",
                "searchPlaceholder": "搜索...",
                "url": "",
                "emptyTable": "表中数据为空",
                "loadingRecords": "载入中...",
                "infoThousands": ",",
                "paginate": {
                    "first": "首页",
                    "previous": "上页",
                    "next": "下页",
                    "last": "末页"
                },
                "aria": {
                    paginate: {
                        first: '首页',
                        previous: '上页',
                        next: '下页',
                        last: '末页'
                    },
                    "sortAscending": ": 以升序排列此列",
                    "sortDescending": ": 以降序排列此列"
                },
                "decimal": "-",
                "thousands": "."
            }
        });

        //修改资产加载数据
         jQuery('#dialog').on('show.bs.modal',function (event) {
             var button = jQuery(event.relatedTarget);
             var title = button.data('title');
             var btn_txt = button.data('btn-txt');
             var url = button.data('url');
             var name = button.data('name')
             if (name == "monitor" || name == "cmd"){
                 jQuery('.modal-dialog').addClass('modal-lg')
             }else{
                 jQuery('.modal-dialog').removeClass('modal-lg')
             }
             var that = this;

             jQuery(that).find('.modal-title').text(title);
             jQuery(that).find('.dialog-commit').text(btn_txt) ;
             jQuery(that).find('.modal-body').load(url)

//             jQuery.get(url,{},function (data) {
//                 jQuery(that).find('.modal-body') .html(data);
//             })

         })

        //修改资产提交返回弹窗
        jQuery('.dialog-commit').on('click',function () {
            var _form = jQuery('#dialog').find('form');
            var url = _form.attr('action')
            var params = _form.serialize()          /*获取提交的信息 name为key  值为value*/
            jQuery.post(url,params,function (data) {
                if (data['is_ok']){
                    swal({
                         title: data['success'],
                         text: '',
                         type: "success",
                         showCancelButton: false,
                         confirmButtonColor: "#DD6B55",
                         confirmButtonText: "确认",
                         cancelButtonText: "关闭",
                         closeOnConfirm: true,
                         closeOnCancel: false
                    },
                    function(isConfirm){
                        window.location.reload()
                    });
                }else{
                    swal({
                         title: "错误信息",
                         text: data['error'],
                         type: "error",
                         showCancelButton: false,
                         confirmButtonColor: "#DD6B55",
                         confirmButtonText: "确认",
                         cancelButtonText: "关闭",
                         closeOnConfirm: true,
                         closeOnCancel: false
                    },
                    function(isConfirm){

                    });
                }
            })
        })

        //删除资产
        jQuery('.del-assets').click(function() {
            var that = this
            var id = jQuery(that).data('id')
            var text = jQuery(that).data('text')
            console.log(id)
            swal({
                title: "您确定要删除吗？",
                text: "您确定要删除"+text+"这条数据？",
                type: "warning",
                showCancelButton: true,
                closeOnConfirm: false,
                confirmButtonText: "是的，我要删除",
                cancelButtonText: "不是,我点错了",
                confirmButtonColor: "#ec6c62"
            }, function() {
                jQuery.post("/assets/delete/", {id: id}, function(data) {
                    location.reload();
                })
            });
        })

        //重置用户密码


})