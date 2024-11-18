drop table if exists ProductInventorySummary
create table ProductInventorySummary (
ProductInventorySummary_ID	int identity (1,1) PRIMARY KEY,
ProductID					int,
--ProductName					nvarchar (250),
TotalQuantity				int)


create procedure sp_ProductInventorySummary1 as
begin
	declare @productIdList table (ProductId int) 
	declare @productId int

	insert into @productIdList 
	select distinct ProductID
	from [Production].[ProductInventory]

	set @productId = (select min(ProductId)
					from @productIdList)

	while @productId <= (select max(ProductId)
					from @productIdList)
	begin
		insert into ProductInventorySummary
		select distinct ppi.ProductID
				, SUM(ppi.Quantity) as TotalQuantity
		from [Production].[ProductInventory] ppi
		where ppi.ProductID = @productId
		group by ppi.ProductID

		delete from @productIdList
		where ProductID = @productId

		set @productId = (select min(ProductId)
						from @productIdList)
	end
end

exec sp_ProductInventorySummary1


