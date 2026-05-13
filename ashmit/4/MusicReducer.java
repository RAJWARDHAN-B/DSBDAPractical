package p4_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Reducer;

public class MusicReducer
        extends Reducer<Text, Text, Text, Text>
{

    public void reduce(Text key,
                       Iterable<Text> values,
                       Context context)
            throws IOException, InterruptedException
    {

        int radioCount = 0;
        int skipCount = 0;

        for (Text val : values)
        {

            String[] parts = val.toString().split(",");

            int radio = Integer.parseInt(parts[0]);
            int skip = Integer.parseInt(parts[1]);

            radioCount += radio;
            skipCount += skip;
        }

        String result =
                "Radio Count = " + radioCount
                + " , Skip Count = " + skipCount;

        context.write(
                key,
                new Text(result)
        );
    }
}