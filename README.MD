# DATA Platform – ETL Pipeline
### Översikt
Detta projekt implementerar en enkel men komplett ETL-pipeline (Extract, Transform, Load) för att bearbeta produktdata från en CSV-fil.


Syftet är att demonstrera hur rådata kan:
- hämtas
- rensas och valideras
- och förberedas för vidare analys eller lagring i databas




## ETL Process
1. Extract: Läser in CSV-filen till en Pandas DataFrame.
2. Transform: Rensar och konverterar kolumner, t.ex. strängar, numeriska värden.
3. Flag/Reject: Markerar produkter med problem:
   - Saknad valuta
   - Negativt pris
   - Extremt högt pris
   - Pris = 0
4. Load: Sparar clean-data i:
   - CSV-fil för analys (`analytics_summary.csv`)
   - SQL-databas (PostgreSQL)