import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Load and parse the XML
tree = ET.parse('export.xml')
root = tree.getroot()

# Extract weight and body fat %
records = []
for record in root.findall('Record'):
    record_type = record.get('type')
    if record_type in ['HKQuantityTypeIdentifierBodyMass', 'HKQuantityTypeIdentifierBodyFatPercentage']:
        records.append({
            'type': record_type,
            'startDate': record.get('startDate'),
            'value': float(record.get('value')),
            'unit': record.get('unit')
        })

df = pd.DataFrame(records)
df['startDate'] = pd.to_datetime(df['startDate'])
df_pivot = df.pivot_table(index='startDate', columns='type', values='value', aggfunc='mean')
df_pivot = df_pivot.rename(columns={
    'HKQuantityTypeIdentifierBodyMass': 'Weight (kg)',
    'HKQuantityTypeIdentifierBodyFatPercentage': 'Body Fat %'
})
df_pivot = df_pivot.sort_index().dropna(how='all')

# Plot
df_pivot.plot(title="Apple Health Weight and Body Fat % Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid()
plt.show()
