$(document).ready(function() {
   $('#libros').bootstrapTable({
      url: "/api/libros/",
      responseHandler: function(data) {
        return {'total': data['count'], 'rows': data['results']}
      },
      pagination: true,
      sidePagination: 'server',
      pageSize: 10,
      pageList: [5, 10, 25, 50],
      queryParamsType: 'no_limit',
      queryParams: function(params) {
        return {
            'search': params.searchText,
            'page_size': params.pageSize,
            'page': params.pageNumber
        }
      },
      search: true,
      trimOnSearch: false,
   });
});
