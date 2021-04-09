for cdx in $(ls ./crawl/list/* | sort);
do
    echo $cdx;
    python download_warc.py $cdx -o crawl/warc -r crawl/rec

    echo '---------------------------------------------------------------------'
    echo '---------------------------------------------------------------------'
    echo '---------------------------------------------------------------------'

    echo 'finished' $cdx;
    # sleep 60
done
