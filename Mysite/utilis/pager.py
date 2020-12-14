class Pager:
    def __init__(self, current_page, per_page, all_datas_num, base_url, show_page=5):
        """
        :param current_page: 当前页
        :param per_page: 每页数据量
        :param all_datas_num: 数据总数
        :param show_page: 页面上显示多少个页码，默认11个
        """
        try:
            self.current_page = int(current_page)
        except Exception:
            self.current_page = 1
        self.per_page = per_page

        a, b = divmod(all_datas_num, self.per_page)
        if b:
            a += 1
        self.total_pages = a
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page - 1) * self.per_page
    
    def end(self):
        return self.current_page * self.per_page
    
    def pager(self):
        page_list = []
        half = self.show_page // 2
        # 总数据量比页码还少
        if self.total_pages < self.show_page:
            begin = 1
            stop = self.total_pages + 1
        # 当前页比half小，如 1-5页
        elif self.current_page <= half:
            begin = 1 
            stop = self.show_page + 1
        # 当前页+half大于总页数，如 27-31页
        elif self.current_page + half > self.total_pages:
            begin = self.total_pages - self.show_page + 1
            stop = self.total_pages + 1
        else:
            begin = self.current_page - half
            stop = self.current_page + half + 1

        if self.current_page <= 1:
            prev_page = '<li class="page-item disabled"><a class="page-link" href="#" tabindex="-1" aria-disabled="true">上一页</a></li>'
        else:
            prev_page = '<li class="page-item"><a class="page-link" href="{0}?page={1}">上一页</a></li>'.format(self.base_url, self.current_page - 1)
        page_list.append(prev_page)

        for page in range(begin, stop):
            if page == self.current_page:
                a_tag = '<li class="page-item active"><a class="page-link" href="{0}?page={1}">{2}</a></li>'.format(self.base_url, page, page)
            else:
                a_tag = '<li class="page-item"><a class="page-link" href="{0}?page={1}">{2}</a></li>'.format(self.base_url, page, page)
            page_list.append(a_tag)
        
        if self.current_page >= self.total_pages:
            next_page = '<li class="page-item disabled"><a class="page-link" href="#" tabindex="-1" aria-disabled="true">下一页</a></li>'
        else:
            next_page = '<li class="page-item"><a class="page-link" href="{0}?page={1}">下一页</a></li>'.format(self.base_url, self.current_page + 1)
        page_list.append(next_page)

        return "".join(page_list)