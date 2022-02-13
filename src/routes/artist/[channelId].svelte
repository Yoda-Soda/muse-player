<script>
	import { page } from '$app/stores';
	import { onMount } from 'svelte';

	let artistData;
	onMount(async () => {
		const response = await fetch('http://0.0.0.0:4231/artist/' + $page.params.channelId);
		const data = await response.json();
		artistData = data;
	});
</script>

{#if artistData == undefined}
	loading data
{:else}
	<img src={artistData.thumbnails[1].url} alt={artistData.name} />
	<p>
		{artistData.name}
	</p>
{/if}
