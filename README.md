# Building the IRS Master Index File

## Background

Currently we track nonprofits using files like the Business Master File or the Exempt Organizations List. There are many limitations to these files:

*	Data on the nonprofits is scattered across the BMF, SOI, 990 Returns, 990-EZ Returns, 990-N (postcard) Returns, the Revocation Database, and other files.
*	They only include the most recent information, so any changes to locations, activities, etc. are lost.
*	There is no historic overview and thus no way to track nonprofits.

The Master Index File is intended to provide a way to track and search all nonprofit returns in a single location to provide some basic reports on their operational status and 990 reporting. It will contain one row of data for each record we have of a nonprofit IRS filing, including amended filings and revocation records.
The intended use would be used to query active or dead organizations, and generate reports on 990 filing behaviors, and create a research sample framework that necessitates a document containing the universe of organizations.

## Included Fields

*	Unique ID (Bridge or something else?)
*	EIN
*	Group Exemption Number
*	Nonprofit Name
*	DBA
*	501c Status
*	Organization type (corporation, partnership, association, trust, etc.)?
*	Filing Date
*	Fiscal Year
*	Accounting Method (cash, accrual, other)
*	NTEE Code
*	Ruledate (most recent ruledate if revoked and reinstated)
*	Closure date (auto revoke, voluntary closure, merger)
*	Address
*	City
*	State
*	Zip
*	Geocodes (use API to create, or add from NCCS BMF)
  *	FIPS
  *	MSA
  *	LAT,LON
*	Website ?
*	Form (990, 990-EZ, 990-N, 990-PF, Auto Revoke, Voluntary Closure)
*	Amended Return? (Y/N)
*	Final Return / Termination? (Y/N)  
*	E-File (Y/N)
*	Data Source (which database was used to generate this row of data?)

### Possible additional fields

*	Basic Filing Overview (Include any of these? They are useful for sampling purposes)
  * Total Revenue
  * Total Expenses
  * Assets BOY
  * Assets EOY
  * Number of Employees
  * Number of Volunteers
  * Number of people with comp > $100k
*	Affiliation Code? (parent, federation, subsidiary, etc)
*	Other activity codes? (see NCCS data dictionary for examples)
*	Prepared by Accountant (Y/N)
*	Audited (Y/N)
*	Schedule A (Y/N)
*	Schedule B (Y/N)
*	Schedule C (Y/N)…Etc.

## Sources

* [NCCS Core files (will not include postcard filers) and BMF files](http://nccs-data.urban.org/index.php)
* [IRS Postcard Filers](https://github.com/Nonprofit-Open-Data-Collective/irs-990n-postcard-filers/blob/master/IRS_990N_Postcard_Filers.RMD)
* [IRS Status Revocation Database](https://github.com/Nonprofit-Open-Data-Collective/irs-revoked-exempt-orgs/blob/master/IRS_Revoked_Exempt_Orgs.RMD)
* [IRS E-File Index (this info might be noted elsewhere)](https://github.com/lecy/Open-Data-for-Nonprofit-Research/blob/master/Open_Nonprofit_Datasets/IRS_E-Filers_Index.Rmd)

### Additional Sources

* [Current Exempt Organizations](https://github.com/Nonprofit-Open-Data-Collective/irs-current-exempt-orgs-database/blob/master/IRS-Current-Exempt-Orgs-List.rmd)
  * Should be redundant with NCCS BMF files but worth double-checking
* [IRS Business Master Files](https://github.com/Nonprofit-Open-Data-Collective/irs-exempt-org-business-master-file/blob/master/IRS-Business-Master-File.rmd)
  * Should be redundant with NCCS Core files but worth double-checking
* [IRS SOI Extracts](https://github.com/lecy/Open-Data-for-Nonprofit-Research/blob/master/Open_Nonprofit_Datasets/IRS_Statistics_of_Income_Files.Rmd)
  * Should be redundant with NCCS Core files but worth double-checking
* [NCCS Data Guide](http://nccs-data.urban.org/NCCS-data-guide.pdf)
