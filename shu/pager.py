class Pagination(object):
    def __init__(self,totalCount,currentPage,perPageItemNumber=30,maxPageNum=7):
        # 数据总个数
        self.total_count = totalCount
        #当前页
        try:
            self.currentPage = int(currentPage)
        except Exception as E:
            self.currentPage = 1
        # 每页显示的行数
        self.perPageItemNumber = perPageItemNumber
        # 最多显示页码
        self.maxPageNum = maxPageNum
