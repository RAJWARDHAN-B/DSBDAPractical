package p5_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Reducer;

public class MovieReducer
        extends Reducer<Text,
                        FloatWritable,
                        Text,
                        FloatWritable>
{

    public void reduce(Text key,
                       Iterable<FloatWritable> values,
                       Context context)
            throws IOException, InterruptedException
    {

        float sum = 0;
        int count = 0;

        for (FloatWritable val : values)
        {

            sum += val.get();
            count++;
        }

        float average = sum / count;

        context.write(
                key,
                new FloatWritable(average)
        );
    }
}