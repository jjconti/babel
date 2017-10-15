$(document).ready(function() {
   $('#libros').bootstrapTable({
      url: "/api/libros/",
      responseHandler: function(data) {
        return {'total': data['count'], 'rows': data['results']}
      },
      pagination: true,
      sidePagination: 'server',
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
