drop table if exists ProductInventorySummary
create table ProductInventorySummary (
ProductInventorySummary_ID	int identity (1,1) PRIMARY KEY,
ProductID					int,
--ProductName					nvarchar (250),
TotalQuantity				int)


create procedure sp_ProductInventorySummary as
begin
insert into ProductInventorySummary
select distinct ppi.ProductID
		, SUM(ppi.Quantity) OVER (PARTITION BY ppi.ProductId) as TotalQuantity
from [Production].[ProductInventory] ppi
end

exec sp_ProductInventorySummary

--select * from ProductInventorySummary