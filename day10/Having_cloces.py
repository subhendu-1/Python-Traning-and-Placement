# select deptno,avg(sal)
# from scott.emp
# group by deptno
# having avg(sal)>2000;



# # order by clause


# select empno,ename,sal from scott.emp order by sal desc;


# # distinct clause

# select distinct deptno from scott.emp;

# simplest join
# select e.empno, e.ename,e.deptno,d.loc
# from scott.emp e,scott.dept d
# where e.deptno=d.deptno;


# # question

# select e.emmpno,e.ename,e.deptno,d.dname,d.loc
# from scott.emp e RIGHT OUTER JOIN, scott.dept d
# ON e.deptno=d.deptno
# where e.empno is null;